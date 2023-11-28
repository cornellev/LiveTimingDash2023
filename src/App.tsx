import './App.css'
import { SocketProvider } from './SocketProvider'
import Lapping from './Lapping'

function App() {
  return (
    <>
      <SocketProvider>
        <Lapping />
      </SocketProvider>
    </>
  )
}

export default App
