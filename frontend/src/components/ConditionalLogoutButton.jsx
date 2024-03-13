import React from "react";
import { useLocation } from "react-router-dom";
import LogoutButton from "./LogoutButton";

function ConditionalLogoutButton() {
  const location = useLocation();
  // Determine if the current location is one of the screens where the logout button should be hidden
  const hideLogoutButton = ["/signIn", "/signUp", "/"].includes(
    location.pathname
  );

  if (hideLogoutButton) {
    return null; // Don't render anything if we're on one of the specified screens
  }

  return <LogoutButton />;
}

export default ConditionalLogoutButton;
