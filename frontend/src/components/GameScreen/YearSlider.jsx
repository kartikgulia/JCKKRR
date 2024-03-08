import React, { useState } from "react";
import PropTypes from "prop-types";

const YearSlider = ({ min, max, onChange }) => {
  const [value, setValue] = useState(min);

  const handleChange = (newValue) => {
    let validValue;
    if (newValue === "" || newValue === null) {
      validValue = null;
    } else {
      validValue = Math.max(min, Math.min(max, Number(newValue)));
    }
    setValue(validValue);
    onChange(validValue);
  };

  return (
    <div style={{ padding: "20px", backgroundColor: "#4d0066",}}>
      <input
        type="number"
        value={value === null ? "" : value}
        onChange={(e) => handleChange(e.target.value)}
        min={min}
        max={max}
        style={{ marginBottom: "20px", width: "100%"}}
      />
      <input
        type="range"
        min={min}
        max={max}
        value={value === null ? "" : value}
        onChange={(e) => handleChange(e.target.value)}
        style={{ width: "100%" }}
      />
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          marginTop: "8px",
        }}
      >
        <span style={{color: "#b76fe4",}}>{min}</span>

        <span style={{color: "#b76fe4",}}>{max}</span>
      </div>
    </div>
  );
};

YearSlider.propTypes = {
  min: PropTypes.number.isRequired,
  max: PropTypes.number.isRequired,
  onChange: PropTypes.func.isRequired,
};

export default YearSlider;
