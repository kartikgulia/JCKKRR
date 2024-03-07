import React from "react";
import PropTypes from "prop-types";

const BackgroundImage = ({ src, onClick, onLoad }) => {
  const style = {
    maxWidth: "100%",
    maxHeight: "50vh",
    position: "relative",
  };

  return <img src={src} style={style} onClick={onClick} alt="" onLoad={onLoad}/>;
};

BackgroundImage.propTypes = {
  src: PropTypes.string.isRequired, // Ensure src is a required string prop
};

export default BackgroundImage;
