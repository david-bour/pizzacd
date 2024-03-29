import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({providedIn: 'root'})
export class AppService {
    constructor(private http: HttpClient) { }

    accounts(): Observable<String[]> {
        return this.http.get<{result: String[]}>('/api/accounts/').pipe(
            map(resp => resp.result)
        )
    }

    getCache(topic: string) {
        return this.http.get<{result: string}>(`/api/cache/${topic}`).pipe(
            map(resp => resp.result)
        )
    }

    createCache(topic: string) {
        return this.http.post<{result: string}>(`/api/cache/${topic}`, {}).pipe(
            map(resp => resp.result)
        )
    }
}
