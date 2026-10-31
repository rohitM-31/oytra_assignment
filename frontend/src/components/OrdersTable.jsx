
import { useMemo, useState } from "react";

const orders = [
  {
    id: "KT100193",
    customer: "Lakshmi Shaikh",
    city: "Chennai",
    amount: 349,
    risk: 18,
    action: "SHIP AS-IS",
    status: "Delivered",
  },
  {
    id: "KT101714",
    customer: "Tanvi Das",
    city: "Indore",
    amount: 898,
    risk: 68,
    action: "MANUAL REVIEW",
    status: "Review",
  },
  {
    id: "KT101825",
    customer: "Rahul Sharma",
    city: "Hyderabad",
    amount: 649,
    risk: 34,
    action: "WHATSAPP CONFIRM",
    status: "Confirmation",
  },
  {
    id: "KT101932",
    customer: "Priya Reddy",
    city: "Bengaluru",
    amount: 749,
    risk: 42,
    action: "PREPAID NUDGE",
    status: "Prepaid nudge",
  },
  {
    id: "KT102014",
    customer: "Amit Kumar",
    city: "Pune",
    amount: 549,
    risk: 9,
    action: "SHIP AS-IS",
    status: "Delivered",
  },
];

function OrdersTable() {
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("All");

  const filteredOrders = useMemo(() => {
    return orders.filter((order) => {
      const searchMatch =
        order.id.toLowerCase().includes(search.toLowerCase()) ||
        order.customer.toLowerCase().includes(search.toLowerCase()) ||
        order.city.toLowerCase().includes(search.toLowerCase());

      const filterMatch =
        filter === "All" || order.status === filter;

      return searchMatch && filterMatch;
    });
  }, [search, filter]);

  const currency = (amount) =>
    new Intl.NumberFormat("en-IN", {
      style: "currency",
      currency: "INR",
      maximumFractionDigits: 0,
    }).format(amount);

  function getActionClass(action) {
    if (action === "SHIP AS-IS") return "action-green";
    if (action === "WHATSAPP CONFIRM") return "action-blue";
    if (action === "PREPAID NUDGE") return "action-purple";
    return "action-orange";
  }

  return (
    <>
      <div className="table-controls">
        <input
          type="text"
          placeholder="Search order, customer or city..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <select
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
        >
          <option value="All">All decisions</option>
          <option value="Delivered">Ship as-is</option>
          <option value="Confirmation">WhatsApp confirmation</option>
          <option value="Prepaid nudge">Prepaid nudge</option>
          <option value="Review">Manual review</option>
        </select>
      </div>

      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ORDER ID</th>
              <th>CUSTOMER</th>
              <th>CITY</th>
              <th>ORDER VALUE</th>
              <th>RTO RISK</th>
              <th>RECOMMENDED ACTION</th>
            </tr>
          </thead>

          <tbody>
            {filteredOrders.map((order) => (
              <tr key={order.id}>
                <td className="order-id">{order.id}</td>
                <td>{order.customer}</td>
                <td>{order.city}</td>
                <td>{currency(order.amount)}</td>

                <td>
                  <div className="risk-cell">
                    <div className="risk-track">
                      <div
                        className={`risk-fill ${
                          order.risk >= 60
                            ? "high"
                            : order.risk >= 25
                            ? "medium"
                            : "low"
                        }`}
                        style={{ width: `${order.risk}%` }}
                      />
                    </div>
                    {order.risk}%
                  </div>
                </td>

                <td>
                  <span className={`action-badge ${getActionClass(order.action)}`}>
                    {order.action}
                  </span>
                </td>
              </tr>
            ))}

            {filteredOrders.length === 0 && (
              <tr>
                <td colSpan="6" className="empty-state">
                  No matching orders found.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default OrdersTable;
