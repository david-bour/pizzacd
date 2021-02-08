import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AppService } from './app.service';
import { Observable } from 'rxjs';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'client';
  names$: Observable<String[]>;
  topic: string = '';

  form = new FormGroup({
    topic: new FormControl(''),
  });

  cacheForm = new FormGroup({
    topic: new FormControl(''),
  });

  constructor(private appservice: AppService) {
    this.names$ = this.appservice.accounts();
  }

  getCache() {
    const { topic } = this.cacheForm.value;
    this.appservice.getCache(topic).subscribe(
      (val) => {
        this.topic = val;
      });
  }

  saveCache() {
    const { topic } = this.form.value;
    this.appservice.createCache(topic).pipe(first()).subscribe();
  }
}
