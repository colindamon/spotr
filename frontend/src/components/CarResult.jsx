import React from 'react';
import { Card, Button, Spinner } from 'react-bootstrap';

const CarResult = ({ predClass, onShowSpecs, specLoading }) => {
  if (!predClass) return null;

  return (
    <Card className="shadow-sm mb-4">
      <Card.Body>
        <h4 className="text-center text-success">Car Identified!</h4>
        <p className="text-center lead">{predClass}</p>
        <div className="d-flex justify-content-center">
          <Button
            variant="info"
            onClick={onShowSpecs}
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
  );
};

export default CarResult;
