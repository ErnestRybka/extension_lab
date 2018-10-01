node {
    def app

    stage('Clone repository locally') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }
}

node('box2'){

    stage('Clone repository on slave') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm

    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("rybkaer/extension_lab_backend1")
    }
    stage('stop/delite all containers'){
        docker.stop.all
        docker.remove.all
    }


    stage('run image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
        docker.run("rybkaer/extension_lab_backend1")
    }
    
}
