import { useEffect, useState, createContext } from "react";

const ws = new WebSocket("URL_HERE")
export const SocketContext = createContext(ws)

interface ISocketProvider {
  children: React.ReactNode
}

export const SocketProvider = (provider: ISocketProvider) => (
  <SocketContext.Provider value={ws}>{provider.children}</SocketContext.Provider>
)