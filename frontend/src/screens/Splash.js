// src/WelcomePage.js
function Splash() {
  return (
    <div>
      <h1>Welcome</h1>
      <button onClick={() => (window.location.href = "/signin")}>
        Sign In
      </button>
    </div>
  );
}

export default Splash;
