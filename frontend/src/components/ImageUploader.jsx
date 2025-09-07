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
        <Form.Label>Choose a car image...</Form.Label>
        <Form.Control type="file" accept="image/*" onChange={handleFileChange} />
      </Form.Group>
      
      {error && <Alert variant="danger">{error}</Alert>}
      
      {imagePreview && (
        <div className="mb-3">
          <h5 className="text-center">Image Preview</h5>
          
          {showCropper ? (
            <div className="mb-3">
              <ReactCrop
                crop={crop}
                onChange={(_, percentCrop) => setCrop(percentCrop)}
                onComplete={(c) => setCompletedCrop(c)}
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
                <Button variant="outline-primary" onClick={applyCrop} disabled={!completedCrop}>
                  Apply Crop
                </Button>
                <Button variant="outline-secondary" onClick={() => setShowCropper(false)}>
                  Cancel
                </Button>
              </div>
            </div>
          ) : (
            <div>
              <div className="d-flex justify-content-center mb-3">
                <img src={imagePreview} alt="Preview" style={{ maxWidth: '100%', maxHeight: '400px' }} />
              </div>
              <div className="d-flex justify-content-center gap-2">
                <Button variant="outline-primary" onClick={() => setShowCropper(true)}>
                  Crop Image
                </Button>
                {originalFile && imagePreview !== URL.createObjectURL(originalFile) && (
                  <Button variant="outline-secondary" onClick={resetCrop}>
                    Reset Crop
                  </Button>
                )}
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
