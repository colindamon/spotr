import React from 'react';
import { Button, Spinner } from 'react-bootstrap';

const CarIdentifier = ({ onIdentify, loading, disabled }) => {
  return (
    <div className="d-flex justify-content-center mt-3">
      <Button
        variant="success"
        onClick={onIdentify}
        disabled={disabled || loading}
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
    </div>
  );
};

export default CarIdentifier;
