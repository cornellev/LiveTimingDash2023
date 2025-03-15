import { useState, useEffect } from "react";
import "./App.css";
import Lapping from "./Lapping";
import Header from "./Header";

let SOCKET_URL = "ws://localhost:8000/ws/uc24"; // Use standard WebSocket

function App() {
  const [data, setData] = useState({
    accel: 0,
    gps_lat: 0,
    gps_long: 0,
    left_rpm: 0,
    right_rpm: 0,
    potent: 0,
    temp: 0,
  });

  useEffect(() => {
    console.log("🔌 Connecting to WebSocket:", SOCKET_URL);
    const socket = new WebSocket(SOCKET_URL);

    socket.onopen = () => {
      console.log("✅ WebSocket Connected");
    };

    socket.onmessage = (event) => {
      console.log("📩 Received WebSocket Data:", event.data);
      try {
        const newData = JSON.parse(event.data);
        setData((prevData) => ({
          ...prevData,
          ...newData,
        }));
      } catch (error) {
        console.error("❌ Error Parsing WebSocket Data:", error);
      }
    };

    socket.onerror = (error) => {
      console.error("❌ WebSocket Error:", error);
    };

    socket.onclose = () => {
      console.warn("⚠️ WebSocket Disconnected. Retrying...");
      setTimeout(() => {
        window.location.reload(); // Simple reconnect strategy
      }, 3000);
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <>
      <Header />
      <Lapping
        accel={data.accel}
        right_rpm={data.right_rpm}
        left_rpm={data.left_rpm}
        potent={data.potent}
        temp={data.temp}
      />
    </>
  );
}

export default App;
