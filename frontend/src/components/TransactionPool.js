import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";
import Transaction from "./Transaction";
import { useHistory } from "react-router-dom";
import { API_BASE_URL, SECONDS_JS } from "../config";

const POLL_INTERVAL = 10 * SECONDS_JS;

function TransactionPool() {
  const [transactions, setTransactions] = useState([]);

  let history = useHistory();

  const fetchTransactions = () => {
    fetch(`${API_BASE_URL}/transactions`)
      .then((response) => response.json())
      .then((json) => {
        console.log("Tranactions json", json);
        setTransactions(json);
      });
  };

  useEffect(() => {
    fetchTransactions();

    const intervalId = setInterval(fetchTransactions, POLL_INTERVAL);

    return () => clearInterval(intervalId);
  }, []);

  const fetchMineBlock = () => {
    fetch(`${API_BASE_URL}/blockchain/mine`).then(() => {
      alert("Succes!");

      history.push("/blockchain");
    });
  };

  return (
    <div className="TransactionPool">
      <Link to="/">Home</Link>
      <hr />
      <h3>Transaction Pool</h3>
      <div>
        {transactions.map((transaction) => (
          <div key={transaction.id}>
            <hr />
            <Transaction transaction={transaction} />
          </div>
        ))}
      </div>
      <hr />
      <Button variant="danger" onClick={fetchMineBlock}>
        Mine a block of these transactions
      </Button>
    </div>
  );
}

export default TransactionPool;
