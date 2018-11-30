#include <blazingdb/protocol/calcite/messages/RelNodeBuilder.hpp>
#include <gtest/gtest.h>

#include "utils.hpp"

TEST(RelNodeBuilderTest, SingleCreation) {
    using namespace com::blazingdb::protocol::calcite::plan::messages;

    auto leftTableScanNodeDetachedBuffer =
        factory::CreateTableScanNodeDetachedBuffer({"left", "table"});

    auto leftTableScanNode =
        flatbuffers::GetRoot<RelNode>(leftTableScanNodeDetachedBuffer.data());

    EXPECT_EQ(RelNodeType_TableScan, leftTableScanNode->type());
    EXPECT_NE(nullptr, leftTableScanNode->data());

    auto leftTableScan =
        flatbuffers::GetRoot<TableScan>(leftTableScanNode->data()->Data());

    EXPECT_EQ("left", leftTableScan->qualifiedName()->GetAsString(0)->str());
    EXPECT_EQ("table", leftTableScan->qualifiedName()->GetAsString(1)->str());
}

TEST(RelNodeBuilderTest, SingleNestedCreation) {
    using namespace com::blazingdb::protocol::calcite::plan::messages;

    auto leftTableScanNodeDetachedBuffer =
        factory::CreateTableScanNodeDetachedBuffer({"left", "table"});
    auto rightTableScanNodeDetachedBuffer =
        factory::CreateTableScanNodeDetachedBuffer({"right", "table"});

    auto logicalUnionNodeDetachedBuffer =
        factory::CreateLogicalUnionNodeDetachedBuffer(
            true,
            leftTableScanNodeDetachedBuffer,
            rightTableScanNodeDetachedBuffer);
}

TEST(RelNodeBuilderTest, Main) {
    using namespace blazingdb::protocol::calcite::messages;

    const std::size_t DATA_SIZE = 512;
    std::uint8_t      data[DATA_SIZE];

    RelNodeBuilder relNodeBilder(data);
    relNodeBilder.Build();
}
