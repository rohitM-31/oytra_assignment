
function StatCard({ title, value, subtitle, icon }) {
  return (
    <div className="stat-card">
      <div className="stat-top">
        <span>{title}</span>
        <span className="stat-icon">{icon}</span>
      </div>

      <h2>{value}</h2>

      <p>{subtitle}</p>
    </div>
  );
}

export default StatCard;
