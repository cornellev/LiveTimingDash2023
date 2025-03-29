import React from "react";

interface StatusWidgetProps {
  speed: number;
  batteryLevel: number; // 0-100
  batteryTemp: number;
}

/**
 * A status widget that displays both speed and battery information in circular widgets
 */
export default function StatusWidget({ speed, batteryLevel, batteryTemp}: StatusWidgetProps) {
  // Speed configuration
  const optimalMin = 6;
  const optimalMax = 8;
  const speedColor = speed >= optimalMin && speed <= optimalMax ? "green" : "red";

  // Battery configuration
  const batteryColor = batteryLevel > 20 ? "green" : "red";

  return (
    <div className="status-widget" style={{ 
      display: 'flex', 
      alignItems: 'center', 
      gap: '40px',
      padding: '20px'
    }}>
      {/* Speed Widget */}
      <div className="speed-widget">
        <div className="status-circle" style={{ borderColor: speedColor }}>
          <h1 className="status-value" style={{ color: speedColor }}>
            {speed.toFixed(2)}
          </h1>
          <p className="status-label">mph</p>
        </div>
        <p style={{ fontWeight: 'bold', color: "green", textAlign: 'center' }}>OPTIMAL SPEED: 6.7 MPH</p>
      </div>
      
      {/* Battery Widget */}
      <div className="battery-widget">
        <div className="status-circle" style={{ 
          borderColor: batteryColor,
          position: 'relative'
        }}>
          <h1 className="status-value" style={{ color: batteryColor }}>
            {batteryLevel}%
          </h1>
        </div>
        <p style={{ fontWeight: 'bold', color: "black", textAlign: 'center' }}>BATTERY TEMP: {batteryTemp}</p>
      </div>
    </div>
  );
}