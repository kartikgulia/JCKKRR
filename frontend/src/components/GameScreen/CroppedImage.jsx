import React, { useRef, useEffect } from "react";
import "../../styles/CroppedImage.css";

const CroppedImage = ({ src, targetCoordinates }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    const image = new Image();
    image.onload = () => {
      const [bottomLeft, bottomRight, topLeft, topRight] = targetCoordinates;

      const minX = Math.min(bottomLeft[0], bottomRight[0], topLeft[0], topRight[0]);
      const minY = Math.min(bottomLeft[1], bottomRight[1], topLeft[1], topRight[1]);
      const maxX = Math.max(bottomLeft[0], bottomRight[0], topLeft[0], topRight[0]);
      const maxY = Math.max(bottomLeft[1], bottomRight[1], topLeft[1], topRight[1]);

      const width = maxX - minX;
      const height = maxY - minY;

      // Adjust canvas size to match the cropped area
      canvas.width = width;
      canvas.height = height;

      ctx.drawImage(image, minX, minY, width, height, 0, 0, width, height);
    };

    image.src = src;
  }, [src, targetCoordinates]);

  return (
    <div className="cropped-image-container">
      <canvas ref={canvasRef}></canvas>
    </div>
  );
};

export default CroppedImage;

