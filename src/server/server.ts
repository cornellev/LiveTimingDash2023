import { Server } from 'socket.io';

const port = 5173
const io = new Server(port, {
  connectionStateRecovery: {
    // the backup duration of the sessions and the packets
    maxDisconnectionDuration: 2 * 60 * 1000,
    // whether to skip middlewares upon successful recovery
    skipMiddlewares: true,
  }
})
io.on("connection", (socket) => {
  console.log("server connected")
  console.log(socket.id)
})

export const SendData = (data: JSON) => {
  io.sockets.emit("data-sent", data)
}