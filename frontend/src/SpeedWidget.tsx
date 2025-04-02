import React from "react";

interface SpeedWidgetProps {
  speed: number;
}

/**
 * A status widget that displays both speed and battery information in circular widgets
 */
export default function SpeedWidget({ speed}: SpeedWidgetProps) {
  // Speed configuration
  const optimalMin = 6;
  const optimalMax = 8;
  const speedColor = speed >= optimalMin && speed <= optimalMax ? "green" : "red";

  return (
      <div className="speed-widget" style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
        <div className="speed-circle" style={{ borderColor: speedColor }}>
          <h1 className="speed-value" style={{ color: speedColor }}>
            {speed.toFixed(2)}
          </h1>
          <p className="speed-label">mph</p>
        </div>
        <p style={{ fontWeight: 'bold', color: "green", textAlign: 'center', marginTop: "10px" }}>OPTIMAL SPEED: 6.7 MPH</p>
      </div>
  );
}