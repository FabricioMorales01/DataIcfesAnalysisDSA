import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PredictService {

  constructor(private http: HttpClient) {}

  predict(data) {
    return this.http.post('/api/v1/predict', data);
  }
}
