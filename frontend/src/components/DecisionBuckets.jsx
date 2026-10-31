
const buckets = [
  {
    title: "Ship as-is",
    count: 2,
    description: "Low-risk orders",
    color: "green",
    icon: "↗",
  },
  {
    title: "WhatsApp confirmation",
    count: 1,
    description: "Awaiting customer response",
    color: "blue",
    icon: "✉",
  },
  {
    title: "Prepaid nudge",
    count: 1,
    description: "Offer prepaid discount",
    color: "purple",
    icon: "₹",
  },
  {
    title: "Hold / Manual Review",
    count: 1,
    description: "Needs operations attention",
    color: "orange",
    icon: "!",
  },
];

function DecisionBuckets() {
  return (
    <div className="bucket-grid">
      {buckets.map((bucket) => (
        <div className="bucket-card" key={bucket.title}>
          <div className={`bucket-icon ${bucket.color}`}>
            {bucket.icon}
          </div>

          <div className="bucket-count">{bucket.count}</div>

          <h3>{bucket.title}</h3>

          <p>{bucket.description}</p>
        </div>
      ))}
    </div>
  );
}

export default DecisionBuckets;
