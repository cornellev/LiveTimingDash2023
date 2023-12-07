import './App.css'
import { SocketProvider } from './SocketProvider'
import Lapping from './Lapping'
import BatteryData from './BatteryData'

function App() {
  return (
    <>
      <SocketProvider>
        <Lapping />
        <BatteryData />
      </SocketProvider>
    </>
  )
}

export default App
