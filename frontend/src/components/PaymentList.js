import React, { useState, useEffect } from 'react';

const PaymentList = () => {
  const [payments, setPayments] = useState([]);

  useEffect(() => {
    fetch('/api/payments/')
      .then(response => response.json())
      .then(data => setPayments(data));
  }, []);

  return (
    <div>
      <h2>Payments</h2>
      <ul>
        {payments.map(payment => (
          <li key={payment.id}>{payment.amount} - {payment.status}</li>
        ))}
      </ul>
    </div>
  );
};

export default PaymentList;