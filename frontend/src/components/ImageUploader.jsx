import React, { useState, useRef } from 'react';
import { Form, Button, Alert } from 'react-bootstrap';
import ReactCrop from 'react-image-crop';
import 'react-image-crop/dist/ReactCrop.css';

const ImageUploader = ({ onImageSelect, error }) => {
  const [imagePreview, setImagePreview] = useState(null);
  const [originalFile, setOriginalFile] = useState(null);
  const [crop, setCrop] = useState();
  const [completedCrop, setCompletedCrop] = useState();
  const [showCropper, setShowCropper] = useState(false);
  
  const imgRef = useRef(null);
  const canvasRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setOriginalFile(file);
      onImageSelect(file);
      
      const reader = new FileReader();
      reader.onload = (ev) => setImagePreview(ev.target.result);
      reader.readAsDataURL(file);
    }
  };

  const onImageLoad = (e) => {
    const { width, height } = e.currentTarget;
    setCrop({
      unit: '%',
      width: 80,
      height: 80,
      x: 10,
      y: 10,
    });
  };

  const applyCrop = async () => {
    if (!completedCrop || !imgRef.current) return;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const image = imgRef.current;
    
    const scaleX = image.naturalWidth / image.width;
    const scaleY = image.naturalHeight / image.height;
    
    canvas.width = completedCrop.width * scaleX;
    canvas.height = completedCrop.height * scaleY;
    
    ctx.drawImage(
      image,
      completedCrop.x * scaleX,
      completedCrop.y * scaleY,
      completedCrop.width * scaleX,
      completedCrop.height * scaleY,
      0,
      0,
      completedCrop.width * scaleX,
      completedCrop.height * scaleY
    );

    canvas.toBlob((blob) => {
      if (blob) {
        const croppedFile = new File([blob], 'cropped-car.jpg', { type: 'image/jpeg' });
        const croppedUrl = URL.createObjectURL(blob);
        setImagePreview(croppedUrl);
        onImageSelect(croppedFile);
        setShowCropper(false);
      }
    }, 'image/jpeg', 0.95);
  };

  const resetCrop = () => {
    if (originalFile) {
      onImageSelect(originalFile);
      const reader = new FileReader();
      reader.onload = (ev) => setImagePreview(ev.target.result);
      reader.readAsDataURL(originalFile);
    }
    setShowCropper(false);
  };

  return (
    <>
      <Form.Group className="mb-3">
        <Form.Label style={{ 
          fontSize: '1.1rem', 
          fontWeight: '500',
          color: 'var(--text-primary)',
          marginBottom: '1rem'
        }}>
          📷 Choose a car image...
        </Form.Label>
        <Form.Control 
          type="file" 
          accept="image/*" 
          onChange={handleFileChange}
          style={{
            padding: '0.75rem',
            borderRadius: '0.75rem',
            border: `2px solid var(--border-color)`,
            backgroundColor: 'var(--bg-card)',
            color: 'var(--text-primary)',
            transition: 'all 0.3s ease'
          }}
        />
      </Form.Group>
      
      {error && (
        <Alert variant="danger" style={{ 
          backgroundColor: 'rgba(220, 53, 69, 0.1)',
          color: 'var(--danger)',
          border: 'none',
          borderRadius: '0.75rem'
        }}>
          {error}
        </Alert>
      )}
      
      {imagePreview && (
        <div className="mb-3">
          <h5 className="text-center" style={{ color: 'var(--text-primary)', marginBottom: '1rem' }}>
            Image Preview
          </h5>
          
          {showCropper ? (
            <div className="mb-3">
              {/* Custom ReactCrop with no shadow overlay */}
              <div className="crop-wrapper">
                <ReactCrop
                  crop={crop}
                  onChange={(_, percentCrop) => setCrop(percentCrop)}
                  onComplete={(c) => setCompletedCrop(c)}
                  minWidth={50}
                  minHeight={50}
                  ruleOfThirds
                  className="no-shadow-crop"
                >
                  <img
                    ref={imgRef}
                    alt="Crop me"
                    src={imagePreview}
                    onLoad={onImageLoad}
                    style={{ 
                      maxHeight: '500px', 
                      maxWidth: '100%',
                      display: 'block',
                      borderRadius: '0.5rem'
                    }}
                  />
                </ReactCrop>
              </div>
              
              <div className="d-flex justify-content-center gap-2 mt-3">
                <Button variant="success" onClick={applyCrop}>
                  Apply Crop
                </Button>
                <Button variant="secondary" onClick={resetCrop}>
                  Reset
                </Button>
              </div>
            </div>
          ) : (
            <div className="crop-container text-center">
              <img 
                src={imagePreview} 
                alt="Uploaded car" 
                style={{ 
                  maxHeight: '400px', 
                  maxWidth: '100%', 
                  borderRadius: '0.75rem',
                  boxShadow: 'var(--shadow-md)'
                }} 
              />
              <div className="mt-3">
                <Button 
                  variant="outline-primary" 
                  onClick={() => setShowCropper(true)}
                >
                  Crop Image
                </Button>
              </div>
            </div>
          )}
        </div>
      )}
      
      <canvas ref={canvasRef} style={{ display: 'none' }} />
    </>
  );
};

export default ImageUploader;
