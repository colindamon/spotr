import React, { useState, useRef } from 'react';
import { Container, Row, Col, Card, Button, Alert, Spinner, Form, ListGroup } from 'react-bootstrap';
import ReactCrop from 'react-image-crop';
import 'react-image-crop/dist/ReactCrop.css';
import axios from 'axios';

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

function App() {
  const [imageFile, setImageFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [crop, setCrop] = useState();
  const [completedCrop, setCompletedCrop] = useState();
  const [croppedImageUrl, setCroppedImageUrl] = useState(null);
  const [showCropper, setShowCropper] = useState(false);
  const [predClass, setPredClass] = useState(null);
  const [specs, setSpecs] = useState(null);
  const [loading, setLoading] = useState(false);
  const [specLoading, setSpecLoading] = useState(false);
  const [error, setError] = useState(null);
  
  const imgRef = useRef(null);
  const previewCanvasRef = useRef(null);

  // File upload handler
  function handleFileChange(e) {
    const file = e.target.files[0];
    if (file) {
      setImageFile(file);
      setPredClass(null);
      setSpecs(null);
      setError(null);
      setCroppedImageUrl(null);
      setShowCropper(false);
      const reader = new FileReader();
      reader.onload = (ev) => setImagePreview(ev.target.result);
      reader.readAsDataURL(file);
    }
  }

  // Initialize crop when image loads
  function onImageLoad(e) {
    const { width, height } = e.currentTarget;
    setCrop({
      unit: '%',
      width: 80,
      height: 80,
      x: 10,
      y: 10,
    });
  }

  // Generate cropped image
  function getCroppedImg(image, crop, fileName) {
    const canvas = previewCanvasRef.current;
    const ctx = canvas.getContext('2d');
    
    if (!crop || !canvas || !ctx) {
      return;
    }

    const scaleX = image.naturalWidth / image.width;
    const scaleY = image.naturalHeight / image.height;
    
    canvas.width = crop.width * scaleX;
    canvas.height = crop.height * scaleY;
    
    ctx.imageSmoothingQuality = 'high';
    
    ctx.drawImage(
      image,
      crop.x * scaleX,
      crop.y * scaleY,
      crop.width * scaleX,
      crop.height * scaleY,
      0,
      0,
      crop.width * scaleX,
      crop.height * scaleY
    );

    return new Promise((resolve) => {
      canvas.toBlob((blob) => {
        if (!blob) {
          console.error('Canvas is empty');
          return;
        }
        resolve(blob);
      }, 'image/jpeg', 0.95);
    });
  }

  // Apply crop
  async function handleApplyCrop() {
    if (!completedCrop || !imgRef.current) return;

    try {
      const croppedBlob = await getCroppedImg(imgRef.current, completedCrop, 'cropped.jpg');
      const croppedUrl = URL.createObjectURL(croppedBlob);
      setCroppedImageUrl(croppedUrl);
      
      // Convert blob to file for upload
      const croppedFile = new File([croppedBlob], 'cropped-car.jpg', { type: 'image/jpeg' });
      setImageFile(croppedFile);
      setShowCropper(false);
    } catch (error) {
      setError('Error cropping image: ' + error.message);
    }
  }

  // Reset crop
  function handleResetCrop() {
    setCroppedImageUrl(null);
    setShowCropper(false);
    // Reset to original file
    const fileInput = document.querySelector('input[type="file"]');
    if (fileInput.files[0]) {
      setImageFile(fileInput.files[0]);
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
                  
                  {/* Show cropper when enabled */}
                  {showCropper && (
                    <div className="mb-3">
                      <ReactCrop
                        crop={crop}
                        onChange={(_, percentCrop) => setCrop(percentCrop)}
                        onComplete={(c) => setCompletedCrop(c)}
                        aspect={undefined}
                        minWidth={50}
                        minHeight={50}
                      >
                        <img
                          ref={imgRef}
                          alt="Crop me"
                          src={imagePreview}
                          style={{ maxWidth: '100%', maxHeight: '400px' }}
                          onLoad={onImageLoad}
                        />
                      </ReactCrop>
                      <div className="d-flex justify-content-center gap-2 mt-2">
                        <Button variant="success" onClick={handleApplyCrop} disabled={!completedCrop}>
                          Apply Crop
                        </Button>
                        <Button variant="secondary" onClick={() => setShowCropper(false)}>
                          Cancel
                        </Button>
                      </div>
                    </div>
                  )}
                  
                  {/* Show current image (original or cropped) */}
                  {!showCropper && (
                    <div className="d-flex justify-content-center">
                      <img 
                        src={croppedImageUrl || imagePreview} 
                        alt="Preview" 
                        style={{ maxWidth: '100%', maxHeight: '400px' }} 
                      />
                    </div>
                  )}
                  
                  {/* Control buttons */}
                  {!showCropper && (
                    <div className="d-flex justify-content-center gap-2 mt-3">
                      <Button
                        variant="primary"
                        onClick={handleIdentify}
                        disabled={loading || !imageFile}
                      >
                        {loading ? (
                          <>
                            <Spinner as="span" animation="border" size="sm" className="me-2" />
                            Identifying...
                          </>
                        ) : (
                          'Identify Car'
                        )}
                      </Button>
                      
                      <Button
                        variant="outline-primary"
                        onClick={() => setShowCropper(true)}
                        disabled={loading}
                      >
                        Crop Image
                      </Button>
                      
                      {croppedImageUrl && (
                        <Button
                          variant="outline-secondary"
                          onClick={handleResetCrop}
                          disabled={loading}
                        >
                          Reset Crop
                        </Button>
                      )}
                    </div>
                  )}
                </div>
              )}
            </Card.Body>
          </Card>

          {/* Error display */}
          {error && (
            <Alert variant="danger" className="mb-4">
              {error}
            </Alert>
          )}

          {/* Prediction result */}
          {predClass && (
            <Card className="shadow-sm mb-4">
              <Card.Body>
                <h4 className="text-center text-success">Car Identified!</h4>
                <p className="text-center lead">{predClass}</p>
                <div className="d-flex justify-content-center">
                  <Button
                    variant="info"
                    onClick={handleShowSpecs}
                    disabled={specLoading}
                  >
                    {specLoading ? (
                      <>
                        <Spinner as="span" animation="border" size="sm" className="me-2" />
                        Loading specs...
                      </>
                    ) : (
                      'Show Specifications'
                    )}
                  </Button>
                </div>
              </Card.Body>
            </Card>
          )}

          {/* Specifications */}
          {specs && (
            <Card className="shadow-sm">
              <Card.Body>
                <h4 className="text-center mb-3">Car Specifications</h4>
                <ListGroup variant="flush">
                  {Object.entries(specs).map(([key, value]) => (
                    <ListGroup.Item key={key} className="d-flex justify-content-between">
                      <strong>{key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}:</strong>
                      <span>{value || 'N/A'}</span>
                    </ListGroup.Item>
                  ))}
                </ListGroup>
              </Card.Body>
            </Card>
          )}
        </Col>
      </Row>
      
      {/* Hidden canvas for image cropping */}
      <canvas
        ref={previewCanvasRef}
        style={{ display: 'none' }}
      />
    </Container>
  );
}

export default App;
