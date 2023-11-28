import { useEffect, useState, createContext } from "react";
let SOCKET_URL = "ws://" + location.host
const ws = new WebSocket(SOCKET_URL)
export const SocketContext = createContext(ws)

interface ISocketProvider {
  children: React.ReactNode
}

export const SocketProvider = (props: ISocketProvider) => {
  const [web, setWeb] = useState<WebSocket>(ws)
  useEffect(() => {
    const onClose = () => {
      setTimeout(() => {
        setWeb(new WebSocket(SOCKET_URL))
      }, 30)
    }
    ws.addEventListener("close", onClose)
    return () => {
      ws.removeEventListener("close", onClose)
    }
  }, [web, setWeb])

  return (
    <SocketContext.Provider value={ws}>{props.children}</SocketContext.Provider>
  )
}