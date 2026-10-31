
import { useState } from "react";
import { validateAddress } from "../services/validationService";

function AddressValidation() {
  const [form, setForm] = useState({
    customer_name: "Lakshmi Shaikh",
    address: "Near bus stop",
    city: "Chennai",
    state: "Tamil Nadu",
    pincode: "600084",
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleValidation = async (e) => {
    e.preventDefault();

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const data = await validateAddress(form);
      setResult(data);
    } catch (err) {
      console.error(err);
      setError(
        err.response?.data?.detail
          ? JSON.stringify(err.response.data.detail)
          : "Unable to connect to the backend. Check whether FastAPI is running."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="validation-card">
      <h3>AI Address Validation</h3>
      <p>Validate customer details using Gemini AI</p>

      <form onSubmit={handleValidation}>
        <input
          name="customer_name"
          placeholder="Customer name"
          value={form.customer_name}
          onChange={handleChange}
          required
        />

        <input
          name="address"
          placeholder="Address"
          value={form.address}
          onChange={handleChange}
          required
        />

        <input
          name="city"
          placeholder="City"
          value={form.city}
          onChange={handleChange}
          required
        />

        <input
          name="state"
          placeholder="State"
          value={form.state}
          onChange={handleChange}
          required
        />

        <input
          name="pincode"
          placeholder="PIN code"
          value={form.pincode}
          onChange={handleChange}
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Validating..." : "Validate Address"}
        </button>
      </form>

      {error && <p className="error-message">{error}</p>}

      {result && (
        <div className="validation-result">
          <h4>Gemini Validation Result</h4>

          <p>
            <strong>Name:</strong> {result.name_status}
          </p>

          <p>
            <strong>Address:</strong> {result.address_status}
          </p>

          <p>
            <strong>Risk level:</strong> {result.risk_level}
          </p>

          <p>
            <strong>Reason:</strong> {result.reason}
          </p>

          <p>
            <strong>Recommendation:</strong> {result.suggestion}
          </p>
        </div>
      )}
    </div>
  );
}

export default AddressValidation;
