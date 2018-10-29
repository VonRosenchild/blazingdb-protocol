#ifndef VTable_H
#define VTable_H

#include <iostream>
#include <iomanip>
#include <ios>
#include <vector>
#include <type_traits>
#include <cassert>
#include <cmath>
#include <tuple>
#include <iostream>
#include <utility>

#include "gdf/gdf.h"
#include "vector.h"
#include "column.h"
#include "any.h"

namespace gdf {
namespace library {

class Table {
public:
  Table(const std::string &name) : name_{name} {

  }

  Table(const std::string &name, std::vector<Column *> &columns)
    : name_{name}, columns_{columns} 
    {

    }

  const Column &operator[](const std::size_t i) const { return *columns_[i]; }

  size_t num_columns() const {
    return columns_.size();
  }
  
  size_t num_rows() const {
    return columns_[0]->size();
  }


   

  template <typename StreamType>
  void print(StreamType & stream)
  {
    _size_columns();
    unsigned int cell_padding = 1;
   // Start computing the total width
    // First - we will have num_columns() + 1 "|" characters
    unsigned int total_width = num_columns() + 1;

    // Now add in the size of each colum
    for (auto & col_size : column_sizes_)
      total_width += col_size + (2 * cell_padding);

    // Print out the top line
    stream << std::string(total_width, '-') << "\n";

    std::vector<std::string> headers;
    for (unsigned int i = 0; i < num_columns(); i++)
      headers.push_back(this->columns_[i]->name());

    // Print out the headers
    stream << "|";
    for (unsigned int i = 0; i < num_columns(); i++)
    {
      // Must find the center of the column
      auto half = column_sizes_[i] / 2;
      half -= headers[i].size() / 2;

      stream << std::string(cell_padding, ' ') << std::setw(column_sizes_[i]) << std::left
             << std::string(half, ' ') + headers[i] << std::string(cell_padding, ' ') << "|";
    }

    stream << "\n";

 
    // Print out the line below the header
    stream << std::string(total_width, '-') << "\n";

    // Now print the rows of the VTable
    for (int i = 0; i < num_rows(); i++) {
      stream << "|";

     
      for (int j = 0; j < num_columns(); j++) {
        stream << std::string(cell_padding, ' ') << std::setw(column_sizes_[j])
           << columns_[j]->get_as_str(i) << std::string(cell_padding, ' ') << "|";

      }
      stream << "\n";
    }

    // Print out the line below the header
    stream << std::string(total_width, '-') << "\n";
    
  }

protected:

  void _size_columns()
  {
    column_sizes_.resize(num_columns());

    // Temporary for querying each row
    std::vector<unsigned int> column_sizes(num_columns());

    // Start with the size of the headers
    for (unsigned int i = 0; i < num_columns(); i++)
      column_sizes_[i] = this->columns_[i]->name().size();

  }


private:
  /// Holds the prinVTable width of each column
  std::vector<unsigned int> column_sizes_;
  const std::string name_;
  std::vector<Column *> columns_;
};


class TableBuilder {
public:
  TableBuilder(const std::string &                  name,
               std::initializer_list<ColumnBuilder> builders)
    : name_{name}, builders_{builders} {}

  Table build(const std::size_t length) {
    std::vector<Column *> v;
    for (auto b : builders_) 
      v.push_back(b.column_ptr());
    return Table(name_, v);
  }

private:
  const std::string          name_;
  std::vector<ColumnBuilder> builders_;
};


// helper function to tuple_each a tuple of any size
template<class Tuple, typename Func, std::size_t N>
struct TupleEach {
	static void tuple_each(Tuple& t, Func& f)
	{
		TupleEach<Tuple, Func, N - 1>::tuple_each(t, f);
		f(std::get<N - 1>(t));
	}
};

template<class Tuple, typename Func>
struct TupleEach<Tuple, Func, 1> {
	static void tuple_each(Tuple& t, Func& f)
	{
		f(std::get<0>(t));
	}
};

template<typename Tuple, typename Func>
void tuple_each(Tuple& t, Func&& f)
{
	TupleEach<Tuple, Func, std::tuple_size<Tuple>::value>::tuple_each(t, f);
}
// end helper function


template <class...Ts>
class TableRowBuilder {
public:
  typedef std::tuple<Ts...> DataTuple;

  TableRowBuilder(const std::string &     name,
                  std::vector<std::string> headers,
                  std::initializer_list<DataTuple> rows)
    : name_{name}, headers_(headers), rows_{rows}, ncols_{std::tuple_size<DataTuple>::value}, nrows_{rows.size()}
  {
  }

  Table build() {
    size_t i = 0;
    std::vector< std::vector< linb::any > > values(ncols_, std::vector< linb::any >(nrows_));
    for (DataTuple row : rows_) {
      int j = 0;
      tuple_each(row, [&values, &i, &j](auto &value) {
        values[j][i] = value;
        j++;
      });
      i++;
    }
    std::vector<ColumnBuilderTyped> builders;
    i = 0;
    tuple_each(rows_[0], [this, &values, &builders, &i](auto value) {
      auto name = headers_[i];
      std::vector< decltype(value) >  column_values;
      for (auto &&any_val : values[i]) {
        column_values.push_back( linb::any_cast<decltype(value)>(any_val) );
      }
      ColumnBuilderTyped b(name, column_values);  
      builders.push_back(b);
      i++;
    });

    std::vector<Column *> v;
    for (auto b : builders) 
      v.push_back(b.column_ptr());
    return Table(name_, v);
  }

private:
  const std::string           name_; 
  const size_t                nrows_;
  const size_t                ncols_;
  std::vector<std::string>    headers_;
  std::vector<DataTuple>      rows_;
};

}//container
}//gdf

#endif