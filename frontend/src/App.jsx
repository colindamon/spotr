import React, { useState } from 'react';
import { Container, Row, Col, Card, Alert } from 'react-bootstrap';
import ImageUploader from './components/ImageUploader';
import CarIdentifier from './components/CarIdentifier';
import CarResult from './components/CarResult';
import CarSpecs from './components/CarSpecs';
import { useCarIdentification } from './hooks/useCarIdentification';

function App() {
  const [imageFile, setImageFile] = useState(null);
  const {
    predClass,
    specs,
    loading,
    specLoading,
    error,
    handleIdentify,
    handleShowSpecs,
    reset
  } = useCarIdentification();

  const handleImageSelect = (file) => {
    setImageFile(file);
    reset();
  };

  const onIdentify = () => {
    handleIdentify(imageFile);
  };

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
              <ImageUploader onImageSelect={handleImageSelect} error={error} />
              
              {imageFile && (
                <CarIdentifier 
                  onIdentify={onIdentify} 
                  loading={loading} 
                  disabled={!imageFile}
                />
              )}
              
              {!imageFile && (
                <Alert variant="info">Upload an image of a car to get started!</Alert>
              )}
            </Card.Body>
          </Card>

          <CarResult 
            predClass={predClass} 
            onShowSpecs={handleShowSpecs} 
            specLoading={specLoading} 
          />
          
          <CarSpecs specs={specs} />
          
          <footer className="text-center text-muted mt-4">
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
