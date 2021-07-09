import { BrowserRouter as Router, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import HomeScreen from "./screens/HomeScreen";
import ProductScreen from "./screens/ProductScreen";
import { Container } from "react-bootstrap";
import React from "react";
function App() {
  return (
    <Router className="App">
      <Header />
      <main>
        <Container>
          <Route path="/" component={HomeScreen} exact />
          <Route path={"/product/:id"} component={ProductScreen} />
        </Container>
      </main>
      <Footer />
    </Router>
  );
}

export default App;
