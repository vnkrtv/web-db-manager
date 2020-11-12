USE shopdb

-- Shop's personnel management - 2 users and 1 role
CREATE LOGIN HeadPersonalManager
    WITH PASSWORD = 'Manager1337';
CREATE USER HeadPersonalManager FOR LOGIN HeadPersonalManager;
GO

CREATE LOGIN HRManager
    WITH PASSWORD = 'Manager1337';
CREATE USER HRManager FOR LOGIN HRManager;
GO

CREATE ROLE PersonalManagement AUTHORIZATION HeadPersonalManager;
ALTER ROLE PersonalManagement ADD MEMBER HRManager;
GO

GRANT SELECT, INSERT, UPDATE, DELETE ON dbo.Workers TO HeadPersonalManager;
GRANT SELECT ON dbo.PurchaseView TO HeadPersonalManager;

GRANT SELECT ON dbo.WorkersView TO HRManager;
GO

-- Shop's product management - 2 users and 1 role
CREATE LOGIN ProductManager
    WITH PASSWORD = 'Manager1337';
CREATE USER ProductManager FOR LOGIN ProductManager;
GO

CREATE LOGIN SupplierManager
    WITH PASSWORD = 'Manager1337';
CREATE USER SupplierManager FOR LOGIN SupplierManager;
GO

CREATE ROLE ProductManagement AUTHORIZATION ProductManager;
ALTER ROLE ProductManagement ADD MEMBER SupplierManager;
GO

GRANT SELECT, INSERT, UPDATE, DELETE ON dbo.Products TO ProductManager;
GRANT SELECT, INSERT, UPDATE, DELETE ON dbo.Producers TO ProductManager;

GRANT SELECT, INSERT, UPDATE, DELETE ON dbo.Suppliers TO SupplierManager;
GRANT SELECT ON dbo.Products TO SupplierManager;
GRANT SELECT ON dbo.Producers TO SupplierManager;
GO


-- Shop's customers management - 2 users and 1 role
CREATE LOGIN CustomersManager
    WITH PASSWORD = 'Manager1337';
CREATE USER CustomersManager FOR LOGIN CustomersManager;
GO

CREATE LOGIN DiscountsManager
    WITH PASSWORD = 'Manager1337';
CREATE USER DiscountsManager FOR LOGIN DiscountsManager;
GO

CREATE ROLE CustomersManagement AUTHORIZATION CustomersManager;
ALTER ROLE CustomersManagement ADD MEMBER DiscountsManager;
GO

GRANT SELECT, INSERT, UPDATE, DELETE ON dbo.Customers TO CustomersManager;
GRANT SELECT, INSERT, UPDATE, DELETE ON dbo.PurchaseView TO CustomersManager;
GRANT SELECT, UPDATE ON dbo.DiscountCards TO CustomersManager;

GRANT SELECT, INSERT, UPDATE, DELETE ON dbo.DiscountCards TO DiscountsManager;
GRANT SELECT, UPDATE ON dbo.Customers TO CustomersManager;
GRANT SELECT, UPDATE ON dbo.PurchaseReceipts TO DiscountsManager;
GO