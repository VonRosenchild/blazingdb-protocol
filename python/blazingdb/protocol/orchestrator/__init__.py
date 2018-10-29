import flatbuffers

from blazingdb.protocol.errors import Error
import blazingdb.protocol.transport
import blazingdb.protocol.transport as transport
from blazingdb.messages.blazingdb.protocol.Status import Status
from blazingdb.messages.blazingdb.protocol.ResponseError import ResponseError
from blazingdb.messages.blazingdb.protocol \
  import TableGroup, BlazingTable

from blazingdb.messages.blazingdb.protocol.orchestrator \
  import DMLRequest, DMLResponse, DDLRequest, DDLResponse, DDLCreateTableRequest, DDLDropTableRequest

from blazingdb.messages.blazingdb.protocol.orchestrator.MessageType \
  import MessageType as OrchestratorMessageType

from blazingdb.messages.blazingdb.protocol.interpreter \
  import NodeConnectionInformation

from blazingdb.messages.blazingdb.protocol.orchestrator \
  import AuthRequest, AuthResponse

from blazingdb.protocol.gdf import gdf_columnSchema


class BlazingTableSchema(transport.schema(BlazingTable)):
  name = transport.StringSegment()
  columns = transport.VectorSchemaSegment(gdf_columnSchema)
  columnNames = transport.VectorStringSegment(transport.StringSegment)

class TableGroupSchema(transport.schema(TableGroup)):
  tables = transport.VectorSchemaSegment(BlazingTableSchema)
  name = transport.StringSegment()

class DMLRequestSchema(transport.schema(DMLRequest)):
  query = transport.StringSegment()
  tableGroup = transport.SchemaSegment(TableGroupSchema)

class DDLRequestSchema(transport.schema(DDLRequest)):
  query = transport.StringSegment()

class DDLCreateTableRequestSchema(transport.schema(DDLCreateTableRequest)):
  name = transport.StringSegment()
  columnNames = transport.VectorStringSegment(transport.StringSegment)
  columnTypes = transport.VectorStringSegment(transport.StringSegment)
  dbName = transport.StringSegment()

class DDLDropTableRequestSchema(transport.schema(DDLDropTableRequest)):
  name = transport.StringSegment()
  dbName = transport.StringSegment()

class NodeConnectionInformationSchema(transport.schema(NodeConnectionInformation)):
	path = transport.StringSegment()
	type = transport.NumberSegment()

class DMLResponseSchema(transport.schema(DMLResponse)):
  resultToken = transport.NumberSegment()
  connectionInfo = transport.SchemaSegment(NodeConnectionInformationSchema)

class AuthResponseSchema(transport.schema(AuthResponse)):
  accessToken = transport.NumberSegment()

class AuthRequestSchema(transport.schema(AuthRequest)):
  pass


def BuildDMLRequestSchema(query, tableGroupDto):
  tableGroupName = tableGroupDto['name']
  tables = []
  for index, t in enumerate(tableGroupDto['tables']):
    tableName = t['name']
    columnNames = t['columnNames']
    columns = []
    for i, c in enumerate(t['columns']):
      data = blazingdb.protocol.gdf.cudaIpcMemHandle_tSchema(reserved=c['data'])
      if c['valid'] is None:
        valid = blazingdb.protocol.gdf.cudaIpcMemHandle_tSchema(reserved=b'')
      else:
        valid = blazingdb.protocol.gdf.cudaIpcMemHandle_tSchema(reserved=c['valid'])

      dtype_info = blazingdb.protocol.gdf.gdf_dtype_extra_infoSchema(time_unit=c['dtype_info'])
      gdfColumn = blazingdb.protocol.gdf.gdf_columnSchema(data=data, valid=valid, size=c['size'],
                                dtype=c['dtype'], dtype_info=dtype_info,
                                null_count=c['null_count'])
      columns.append(gdfColumn)
    table = blazingdb.protocol.orchestrator.BlazingTableSchema(name=tableName, columns=columns,
                                 columnNames=columnNames)
    tables.append(table)
  tableGroup = blazingdb.protocol.orchestrator.TableGroupSchema(tables=tables, name=tableGroupName)
  return blazingdb.protocol.orchestrator.DMLRequestSchema(query=query, tableGroup=tableGroup)
