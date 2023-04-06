-- Create a new trigger named 'decrease_quantity'
CREATE TRIGGER decrease_quantity
-- Set trigger to activate after an INSERT into the 'orders' table
BEFORE INSERT ON orders 
FOR EACH ROW UPDATE items
    -- Less the quantity of the item following the order from the 'quantity' column in the 'items' table
SET quantity = quantity - NEW.quantity WHERE id = NEW.item_id;
END;
