import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PredictService {

  constructor(http: HttpClient) {}

  predict(data) {
    return this.http.post('http://172.173.177.148:8000/api/v1/predict', data);
  }
}
