import React, { useState } from 'react';
import { Container, Row, Col, Card, Button, Alert, Spinner, Form, ListGroup } from 'react-bootstrap';
import axios from 'axios';

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

function App() {
  const [imageFile, setImageFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [predClass, setPredClass] = useState(null);
  const [specs, setSpecs] = useState(null);
  const [loading, setLoading] = useState(false);
  const [specLoading, setSpecLoading] = useState(false);
  const [error, setError] = useState(null);

  // File upload handler
  function handleFileChange(e) {
    const file = e.target.files[0];
    if (file) {
      setImageFile(file);
      setPredClass(null);
      setSpecs(null);
      setError(null);
      const reader = new FileReader();
      reader.onload = (ev) => setImagePreview(ev.target.result);
      reader.readAsDataURL(file);
    }
  }

  // Predict handler
  async function handleIdentify() {
    if (!imageFile) return;
    setLoading(true);
    setError(null);
    const formData = new FormData();
    formData.append('file', imageFile, 'car.jpg');
    try {
      const response = await axios.post(`${BACKEND_URL}/predict`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        timeout: 10000,
      });
      setPredClass(response.data.pred_class);
    } catch (err) {
        let details = '';
        if (err.response) {
            details = JSON.stringify(err.response.data);
        } else {
            details = err.message;
        }
        setError('Error identifying car: ' + details);
    } finally {
      setLoading(false);
    }
  }

  // Specs handler
  async function handleShowSpecs() {
    if (!predClass) return;
    setSpecLoading(true);
    setError(null);
    try {
      const response = await axios.get(`${BACKEND_URL}/car-specs`, {
        params: { pred_class: predClass },
        timeout: 10000,
      });
      if (response.data && !response.data.error) {
        setSpecs(response.data);
      } else {
        setError('No specs found or backend error.');
      }
    } catch (err) {
      setError('Error fetching car specs.');
    } finally {
      setSpecLoading(false);
    }
  }

  return (
    <Container className="py-4">
      <Row>
        <Col md={8} className="mx-auto">
          <h1 className="text-center">SpotR 🚗📷</h1>
          <p className="text-center lead">
            Your AI-powered car spotter
          </p>
          <Card className="shadow-sm mb-4">
            <Card.Body>
              <Form.Group className="mb-3">
                <Form.Label>Choose a car image...</Form.Label>
                <Form.Control type="file" accept="image/*" onChange={handleFileChange} />
              </Form.Group>
              {imagePreview && (
                <div className="mb-3">
                  <h5 className="text-center">Image Preview</h5>
                  <div className="d-flex justify-content-center">
                    <img src={imagePreview} alt="Preview" style={{ maxWidth: '100%', maxHeight: '400px' }} />
                  </div>
                  <div className="d-flex justify-content-center mt-3">
                    <Button
                      variant="success"
                      onClick={handleIdentify}
                      disabled={loading}
                    >
                      {loading ? <Spinner size="sm" animation="border" /> : 'Identify Car'}
                    </Button>
                  </div>
                </div>
              )}
              {error && <Alert variant="danger">{error}</Alert>}
              {predClass && (
                <div className="mb-3">
                  <Alert variant="success">Predicted car model: <strong>{predClass}</strong></Alert>
                  <div className="d-flex justify-content-center">
                    <Button variant="primary" onClick={handleShowSpecs} disabled={specLoading}>
                      {specLoading ? <Spinner size="sm" animation="border" /> : 'Search for car specs'}
                    </Button>
                  </div>
                </div>
              )}
              {specs && (
                <>
                  <h6 className="mt-3">Car Specs:</h6>
                  <ListGroup>
                    {Object.entries(specs).map(([key, value]) => (
                      <ListGroup.Item key={key}>
                        <strong>{key}</strong>: {value}
                      </ListGroup.Item>
                    ))}
                  </ListGroup>
                </>
              )}
              {!imageFile && <Alert variant="info">Upload an image of a car to get started!</Alert>}
            </Card.Body>
          </Card>
          <footer className="text-center text-muted">
            <hr />
            <div className="d-flex justify-content-between align-items-center">
              <span>Made by a passionate car enthusiast. ❤️</span>
              <a href="https://github.com/colindamon" target="_blank" rel="noopener noreferrer">
                <img
                  src="https://img.shields.io/badge/colindamon-white?style=flat&logo=github&logoColor=white&logoSize=auto&labelColor=string&color=gray"
                  alt="GitHub"
                  style={{ height: '24px' }}
                />
              </a>
            </div>
          </footer>
        </Col>
      </Row>
    </Container>
  );
}

export default App;
