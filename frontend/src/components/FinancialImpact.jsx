
const financialData = [
  {
    title: "Expected cost per COD RTO",
    value: "₹169.40",
    description: "Shipping, return, handling and expected damage",
  },
  {
    title: "Expected monthly COD RTOs",
    value: "462",
    description: "1,650 COD orders × 28% RTO rate",
  },
  {
    title: "Potential RTO savings",
    value: "Pending calculation",
    description: "Requires actual decision outcomes and counterfactuals",
  },
];

function FinancialImpact() {
  return (
    <div className="financial-grid">
      {financialData.map((item, index) => (
        <div
          className={`financial-card ${index === 2 ? "highlight-card" : ""}`}
          key={item.title}
        >
          <span>{item.title}</span>
          <h2>{item.value}</h2>
          <p>{item.description}</p>
        </div>
      ))}
    </div>
  );
}

export default FinancialImpact;
