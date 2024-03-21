import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormPredictComponent } from './form-predict.component';

describe('FormPredictComponent', () => {
  let component: FormPredictComponent;
  let fixture: ComponentFixture<FormPredictComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FormPredictComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FormPredictComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
