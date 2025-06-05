import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';

import { User } from '../models/user.interface';
import { Product } from '../models/product.interface';
import { Cart } from '../models/cart.interface';

@Injectable({
    providedIn: "root"
})

export class ApiService{
    private apiUrl = "http://localhost:8000/heavenlyvitamin/"

    constructor(private http:HttpClient) {}

    getUser(username: string): Observable<User> {
        return this.http.get<User>(`${this.apiUrl}user/${username}/`);
    }

    getProduct(id: number): Observable<Product> {
        return this.http.get<Product>(`${this.apiUrl}product/${{id}}/`);
    }

    getCart(username: string): Observable<Cart> {
        return this.http.get<Cart>(`${this.apiUrl}user/${username}/cart`)
    }

    validateCredentials(username: string, email: string): Observable<User> {
        return this.http.get<User>(`${this.apiUrl}account/${username}`, {
            params: { username, email }
        });
    }
}