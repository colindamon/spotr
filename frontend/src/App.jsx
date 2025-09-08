import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card, Alert } from 'react-bootstrap';
import ImageUploader from './components/ImageUploader';
import CarIdentifier from './components/CarIdentifier';
import CarResult from './components/CarResult';
import CarSpecs from './components/CarSpecs';
import { useCarIdentification } from './hooks/useCarIdentification';

function App() {
  const [imageFile, setImageFile] = useState(null);
  const [isDarkMode, setIsDarkMode] = useState(true);
  
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

  useEffect(() => {
    const savedTheme = localStorage.getItem('spotr-theme');
    const prefersDark = savedTheme === 'dark' || (!savedTheme && true);
    setIsDarkMode(prefersDark);
    document.documentElement.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
  }, []);

  const toggleTheme = () => {
    const newTheme = !isDarkMode;
    setIsDarkMode(newTheme);
    const themeValue = newTheme ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', themeValue);
    localStorage.setItem('spotr-theme', themeValue);
  };

  const handleImageSelect = (file) => {
    setImageFile(file);
    reset();
  };

  const onIdentify = () => {
    handleIdentify(imageFile);
  };

  return (
    <div className="main-wrapper">
      <button 
        className="theme-toggle"
        onClick={toggleTheme}
        aria-label={`Switch to ${isDarkMode ? 'light' : 'dark'} mode`}
        title={`Switch to ${isDarkMode ? 'light' : 'dark'} mode`}
      >
        <span className="theme-icon">
          {isDarkMode ? '☀️' : '🌙'}
        </span>
      </button>

      <div className="content-wrapper">
        <header className="app-header">
          <Container>
            <h1 className="app-title">SpotR 🚗📷</h1>
            <p className="app-subtitle">
              Your AI-powered car spotting tool
            </p>
          </Container>
        </header>

        <Container className="py-4">
          <Row>
            <Col lg={10} xl={8} className="mx-auto">
              
              <Card className="shadow-sm mb-4">
                <Card.Body>
                  <Card.Title className="text-center mb-4">
                    <span style={{ fontSize: '1.25rem', fontWeight: '600' }}>
                      Upload & Identify Your Car
                    </span>
                  </Card.Title>
                  
                  <ImageUploader onImageSelect={handleImageSelect} error={error} />
                  
                  {imageFile && (
                    <div className="mt-4">
                      <CarIdentifier 
                        onIdentify={onIdentify} 
                        loading={loading} 
                        disabled={!imageFile}
                      />
                    </div>
                  )}
                  
                  {!imageFile && (
                    <Alert variant="info" className="mt-3">
                      <div className="d-flex align-items-center">
                        <span style={{ fontSize: '1.25rem', marginRight: '0.5rem' }}>📸</span>
                        <span>Upload an image of a car to get started with AI-powered identification!</span>
                      </div>
                    </Alert>
                  )}
                </Card.Body>
              </Card>

              <CarResult 
                predClass={predClass} 
                onShowSpecs={handleShowSpecs} 
                specLoading={specLoading} 
              />
              
              <CarSpecs specs={specs} />
              
            </Col>
          </Row>
        </Container>
      </div>

      <footer className="footer">
        <Container>
          <Row>
            <Col md={12}>
              <div className="d-flex flex-column flex-md-row justify-content-between align-items-center">
                <div className="mb-2 mb-md-0">
                  <span style={{ color: 'var(--text-secondary)' }}>
                    🚗 SpotR • Made by a passionate car enthusiast ❤️
                  </span>
                </div>
                <div className="d-flex align-items-center">
                  <a 
                    href="https://github.com/colindamon" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="github-badge"
                  >
                    <img
                      src="https://img.shields.io/badge/colindamon-white?style=flat&logo=github&logoColor=white&logoSize=auto&labelColor=string&color=gray"
                      alt="GitHub Profile"
                      style={{ height: '28px' }}
                    />
                  </a>
                </div>
              </div>
            </Col>
          </Row>
        </Container>
      </footer>
    </div>
  );
}

export default App;