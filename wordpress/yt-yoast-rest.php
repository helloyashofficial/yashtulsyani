<?php
/**
 * Plugin Name: YT Yoast fields over REST
 * Description: Lets the GitHub deploy set Yoast's SEO title, meta description
 *              and focus keyphrase through the WordPress REST API. Without it,
 *              those three fields are pasted into Yoast by hand.
 *
 * Install: upload this file to wp-content/mu-plugins/ (create the folder if it
 * does not exist). Must-use plugins load automatically; there is nothing to
 * activate. Remove the file to undo it.
 *
 * Safe by design: the fields are only writable by a user who can edit that
 * particular post or page, which is exactly who could edit them in Yoast's
 * own panel. Nothing new becomes public.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action( 'init', function () {
	$keys = array( '_yoast_wpseo_title', '_yoast_wpseo_metadesc', '_yoast_wpseo_focuskw' );
	foreach ( array( 'post', 'page' ) as $type ) {
		foreach ( $keys as $key ) {
			register_post_meta( $type, $key, array(
				'type'          => 'string',
				'single'        => true,
				'show_in_rest'  => true,
				'auth_callback' => function ( $allowed, $meta_key, $post_id ) {
					return current_user_can( 'edit_post', $post_id );
				},
			) );
		}
	}
} );
