import './App.css'
import { SocketProvider } from './SocketProvider'
import Lapping from './Lapping'
import BatteryData from './BatteryData'
import CarData from './CarData'

function App() {
  return (
    <>
      <SocketProvider>
        <Lapping />
        <BatteryData />
        <CarData />
      </SocketProvider>
    </>
  )
}

export default App
