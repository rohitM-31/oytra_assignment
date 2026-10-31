
function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="brand">
        <div className="brand-logo">O</div>
        <div>
          <h2>Oytra</h2>
          <span>Risk Intelligence</span>
        </div>
      </div>

      <div className="nav-label">WORKSPACE</div>

      <nav>
        <a className="nav-item active" href="#overview">
          ▦ Overview
        </a>
        <a className="nav-item" href="#orders">
          ▤ Orders
        </a>
        <a className="nav-item" href="#decisions">
          ◈ Risk Decisions
        </a>
        <a className="nav-item" href="#impact">
          ₹ Financial Impact
        </a>
      </nav>

      <div className="sidebar-bottom">
        <div className="system-status">
          <span className="status-dot"></span>
          System online
        </div>

        <div className="profile">
          <div className="avatar">FO</div>
          <div>
            <strong>Founder</strong>
            <span>Admin account</span>
          </div>
        </div>
      </div>
    </aside>
  );
}

export default Sidebar;
