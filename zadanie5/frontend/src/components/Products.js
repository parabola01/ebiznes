import React, { useState, useEffect } from 'react';
import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8080',
});

const Products = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await api.get('/products');
                setProducts(response.data || []);
            } catch (error) {
                console.error('Błąd podczas pobierania produktów:', error);
            }
        };
        fetchProducts();
    }, []);

    return (
        <div>
            <h2>Lista produktów</h2>
            {products.length > 0 ? (
                <ul>
                    {products.map((product) => (
                        <li key={product.id}>
                            {product.name} - {product.price} zł
                        </li>
                    ))}
                </ul>
            ) : (
                <p>Brak produktów do wyświetlenia.</p>
            )}
        </div>
    );
};

export default Products;
