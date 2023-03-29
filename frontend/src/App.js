import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import logo from "./assets/logo.png";
import { API_BASE_URL } from "./config";
import CustomNavbar from "./components/CustomNavbar";
import { Card, Button } from "react-bootstrap";

function App() {
  const [walletInfo, setWalletInfo] = useState({});

  useEffect(() => {
    fetch(`${API_BASE_URL}/wallet/info`)
      .then((response) => response.json())
      .then((json) => setWalletInfo(json));
  }, []);

  const { address, balance } = walletInfo;

  return (
    <div className="App">
      <CustomNavbar />
      <img className="logo" src={logo} alt="logo" />

      <h3>Welcome to pychain</h3>

      <br />
      <Link to="/blockchain">Blockchain</Link>
      <Link to="/conduct-transaction">Conduct a Transaction</Link>
      <Link to="/transaction-pool">Transaction Pool</Link>

      <div className="WalletInfo">
        <Card style={{ width: "50rem" }}>
          <Card.Img variant="top" src="holder.js/100px180" />
          <Card.Body>
            <Card.Title>Address: {address}</Card.Title>
            <Card.Text>Balance: {balance}</Card.Text>
            <Button href="/blockchain" variant="primary">
              Goto Blockchain
            </Button>
          </Card.Body>
        </Card>
      </div>
    </div>
  );
}

export default App;
