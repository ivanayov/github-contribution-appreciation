import { Component } from "@angular/core";
import { HttpClient } from '@angular/common/http';

@Component({
    //styleUrls: ['./wizard.component.scss'],
    templateUrl: './wizard.component.html',
})
export class WizardComponent {

    constructor(private http: HttpClient) {

    }

    open = false;
    loading = false;

    commit: string;
    msg: string;
    from: string
    to: string;

    created = false;
    value = "";

    create() {
        this.loading = true;
        this.open = false;
        setTimeout(() => {
            this.loading = false;
            this.created = true;
        }, 300);

        this.value = "A Kudo from " + this.from + " to " + this.to + " for the commit: " + this.commit + " \n " + this.msg;
    }

    createPullRequest() {
        // api is https://api.github.com/
        // POST /repos/:owner/:repo/pulls

        // head -> string Required. The name of the branch where your changes are implemented.
        // For cross-repository pull requests in the same network, namespace head with a user like this: username:branch.

        // fork the repo first
        // POST /repos/:owner/:repo/forks
        this.http.post("https://api.github.com/repos/tpepper/tpepper.github.io/forks", {}).subscribe((res) => {
            console.log(res);
        }, (err) => {
            // do something clever here
            console.log(err);
        });

        // not working for now -
        this.http.post("https://api.github.com/repos/tpepper/tpepper.github.io/pulls", {
            "title": "Amazing new kudo",
            "body": "Please pull this in!",
            "head": "srusev:tpepper.github.io",
            "base": "master"
        }).subscribe((res) => {
            console.log(res);
        }, (err) => {
            // do something clever here
            console.log(err);
        });
    }
}
