import { Container, Row, Col } from "react-bootstrap";
import React from "react";

function Footer() {
  return (
    <footer>
      <Container>
        <Row>
          <Col className="text-center py-3">
            <p>Copyright &copy;abrsh</p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
}

export default Footer;
