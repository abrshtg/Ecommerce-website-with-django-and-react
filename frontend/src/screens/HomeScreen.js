import React from "react";
import products from "../products.js";
import { Row, Col } from "react-bootstrap";
import Products from "../components/Products.js";
function HomeScreen() {
  return (
    <div>
      <h1>LATEST PRODUCTS</h1>
      <Row>
        {products.map((product) => (
          <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
            <Products product={product} />
          </Col>
        ))}
      </Row>
    </div>
  );
}

export default HomeScreen;
