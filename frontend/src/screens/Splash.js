import "../styles/Splash.css";

function Splash() {
  return (
    <div className="splash-container">
      <h1 className="splash-title">WhereIn</h1>
      <button className="button-style" onClick={() => (window.location.href = "/signIn")}>
        Sign In
      </button>
      <button className="button-style" onClick={() => (window.location.href = "/signUp")}>
        Sign Up
      </button>
    </div>
  );
}

export default Splash;
