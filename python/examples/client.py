import blazingdb.protocol
import blazingdb.protocol.interpreter
import blazingdb.protocol.orchestrator
import blazingdb.protocol.transport.channel

from blazingdb.protocol.interpreter import InterpreterMessage

SESSION_TOKEN = 456


def main():
  connection = blazingdb.protocol.UnixSocketConnection('/tmp/socket')
  client = blazingdb.protocol.Client(connection)

  getResult = blazingdb.protocol.interpreter.GetResultSchema(
    token='RESULT_TOKEN')
  requestBuffer = blazingdb.protocol.transport.channel.MakeRequestBuffer(
    InterpreterMessage.GetResult, SESSION_TOKEN, getResult)

  responseBuffer = client.send(requestBuffer)

  response = blazingdb.protocol.orchestrator.DMLResponseFrom(responseBuffer)

  print(response.payload.token)


if __name__ == '__main__':
  main()
