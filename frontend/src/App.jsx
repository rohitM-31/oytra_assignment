
import Sidebar from "./components/Sidebar";
import StatCard from "./components/StatCard";
import DecisionBuckets from "./components/DecisionBuckets";
import FinancialImpact from "./components/FinancialImpact";
import OrdersTable from "./components/OrdersTable";
import AddressValidation from "./components/AddressValidation";

function App() {
  return (
    <div className="app-layout">

      <Sidebar />

      <main className="main-content" id="overview">

        <header className="topbar">
          <div>
            <p className="eyebrow">OVERVIEW / COD RISK</p>
            <h1>Founder Dashboard</h1>
            <p className="page-description">
              Monitor order risk, operational decisions and business impact.
            </p>
          </div>

          <span className="date-label">30 October 2026</span>
        </header>

        <div className="demo-notice">
          <strong>Demo view</strong>
          <span>
            Sample decisions are illustrative, not live predictions.
          </span>
        </div>

        <section className="section">
          <div className="section-heading">
            <div>
              <h2>Business Snapshot</h2>
              <p>Monthly operating baseline</p>
            </div>
          </div>
          <section className="section" id="validation">
  <AddressValidation />
</section>

          <div className="stats-grid">
            <StatCard
              title="Monthly Orders"
              value="3,000"
              subtitle="Business baseline"
              icon="▦"
            />

            <StatCard
              title="COD Orders"
              value="1,650"
              subtitle="55% of monthly orders"
              icon="₹"
            />

            <StatCard
              title="COD RTO Rate"
              value="28%"
              subtitle="Business baseline"
              icon="↗"
            />

            <StatCard
              title="Monthly COD RTO Cost"
              value="₹78,263"
              subtitle="Estimated baseline"
              icon="₹"
            />
          </div>
        </section>

        <section className="section" id="decisions">
          <div className="section-heading">
            <div>
              <h2>Order Decision Buckets</h2>
              <p>Illustrative sample decisions</p>
            </div>
          </div>

          <DecisionBuckets />
        </section>

        <section className="section" id="impact">
          <div className="section-heading">
            <div>
              <h2>Financial Impact</h2>
              <p>Business estimates</p>
            </div>
          </div>

          <FinancialImpact />
        </section>

        <section className="section" id="orders">
          <div className="section-heading">
            <div>
              <h2>Recent Order Decisions</h2>
              <p>Search and filter sample orders</p>
            </div>
          </div>

          <OrdersTable />
        </section>

        <footer className="footer">
          COD Risk Intelligence Dashboard · Prototype
        </footer>

      </main>
    </div>
  );
}

export default App;
