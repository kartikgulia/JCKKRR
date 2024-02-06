import React, { useState } from "react";
import PropTypes from "prop-types";

const YearSlider = ({ min, max, onChange }) => {
  const [value, setValue] = useState(min);

  const handleChange = (e) => {
    const newValue = e.target.value;
    setValue(newValue);
    onChange(newValue); // Propagate change to parent
  };

  return (
    <div className="YearSliderContainer">
      <div className="CurrentValue">{value}</div>
      <input
        type="range"
        min={min}
        max={max}
        value={value}
        onChange={handleChange}
        className="YearSlider"
        list="tickmarks"
      />
      <datalist id="tickmarks">
        <option value={min} label={min}></option>
        <option value={(max + min) / 2} label={(max + min) / 2}></option>
        <option value={max} label={max}></option>
      </datalist>
    </div>
  );
};

YearSlider.propTypes = {
  min: PropTypes.number.isRequired,
  max: PropTypes.number.isRequired,
  onChange: PropTypes.func.isRequired,
};

export default YearSlider;
