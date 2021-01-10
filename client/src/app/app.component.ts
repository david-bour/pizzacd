import { Component } from '@angular/core';
import { AppService } from './app.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'client';
  names$: Observable<String[]>;

  constructor(private appservice: AppService) {
    this.names$ = this.appservice.accounts();
  }
}
