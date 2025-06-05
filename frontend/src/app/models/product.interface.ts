export interface Product {
    id: number;
    product_name: string;
    description: string;
    brand: string;
    price: number;
    stock: number;
    status: string;
    category: string;
    count: number;
    // product_image: Record<string, any>;
}